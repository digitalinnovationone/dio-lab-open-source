import { editAsync } from 'external-editor';
import { createPrompt, useEffect, useState, useKeypress, usePrefix, isEnterKey, makeTheme, } from '@inquirer/core';
const editorTheme = {
    validationFailureMode: 'keep',
};
export default createPrompt((config, done) => {
    const { waitForUseInput = true, file: { postfix = config.postfix ?? '.txt', ...fileProps } = {}, validate = () => true, } = config;
    const theme = makeTheme(editorTheme, config.theme);
    const [status, setStatus] = useState('idle');
    const [value = '', setValue] = useState(config.default);
    const [errorMsg, setError] = useState();
    const prefix = usePrefix({ status, theme });
    function startEditor(rl) {
        rl.pause();
        const editCallback = async (error, answer) => {
            rl.resume();
            if (error) {
                setError(error.toString());
            }
            else {
                setStatus('loading');
                const isValid = await validate(answer);
                if (isValid === true) {
                    setError(undefined);
                    setStatus('done');
                    done(answer);
                }
                else {
                    if (theme.validationFailureMode === 'clear') {
                        setValue(config.default);
                    }
                    else {
                        setValue(answer);
                    }
                    setError(isValid || 'You must provide a valid value');
                    setStatus('idle');
                }
            }
        };
        editAsync(value, (error, answer) => void editCallback(error, answer), {
            postfix,
            ...fileProps,
        });
    }
    useEffect((rl) => {
        if (!waitForUseInput) {
            startEditor(rl);
        }
    }, []);
    useKeypress((key, rl) => {
        // Ignore keypress while our prompt is doing other processing.
        if (status !== 'idle') {
            return;
        }
        if (isEnterKey(key)) {
            startEditor(rl);
        }
    });
    const message = theme.style.message(config.message, status);
    let helpTip = '';
    if (status === 'loading') {
        helpTip = theme.style.help('Received');
    }
    else if (status === 'idle') {
        const enterKey = theme.style.key('enter');
        helpTip = theme.style.help(`Press ${enterKey} to launch your preferred editor.`);
    }
    let error = '';
    if (errorMsg) {
        error = theme.style.error(errorMsg);
    }
    return [[prefix, message, helpTip].filter(Boolean).join(' '), error];
});
