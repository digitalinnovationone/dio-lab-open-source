/**
 * Inquirer.js
 * A collection of common interactive command line user interfaces.
 */
import { Separator } from '@inquirer/prompts';
import type { Prettify } from '@inquirer/type';
import PromptsRunner from './ui/prompt.ts';
import type { LegacyPromptConstructor, PromptFn } from './ui/prompt.ts';
import type { Answers, CustomQuestion, UnnamedDistinctQuestion, StreamOptions } from './types.ts';
import { Observable } from 'rxjs';
export type { QuestionMap, Question, DistinctQuestion, Answers, PromptSession, } from './types.ts';
type PromptReturnType<T> = Promise<Prettify<T>> & {
    ui: PromptsRunner<Prettify<T>>;
};
/**
 * Create a new self-contained prompt module.
 */
export declare function createPromptModule<Prompts extends Record<string, Record<string, unknown>> = never>(opt?: StreamOptions): {
    <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: ((UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never> | CustomQuestion<PrefilledAnswers & A extends infer T_1 ? { [K in keyof T_1]: (PrefilledAnswers & A)[K]; } : never, Prompts>) & {
        name: Extract<keyof PrefilledAnswers, string> | Extract<keyof A, string>;
    })[], answers?: PrefilledAnswers): PromptReturnType<Prettify<PrefilledAnswers & A>>;
    <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: { [name in keyof A]: UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never> | CustomQuestion<PrefilledAnswers & A extends infer T_1 ? { [K in keyof T_1]: (PrefilledAnswers & A)[K]; } : never, Prompts>; }, answers?: PrefilledAnswers): PromptReturnType<Prettify<PrefilledAnswers & Answers<Extract<keyof A, string>>>>;
    <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: Observable<(UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never> | CustomQuestion<PrefilledAnswers & A extends infer T_1 ? { [K in keyof T_1]: (PrefilledAnswers & A)[K]; } : never, Prompts>) & {
        name: Extract<keyof PrefilledAnswers, string> | Extract<keyof A, string>;
    }>, answers?: PrefilledAnswers): PromptReturnType<Prettify<PrefilledAnswers & A>>;
    <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: (UnnamedDistinctQuestion<A & PrefilledAnswers> | CustomQuestion<A & PrefilledAnswers, Prompts>) & {
        name: Extract<keyof A, string> | Extract<keyof PrefilledAnswers, string>;
    }, answers?: PrefilledAnswers): PromptReturnType<PrefilledAnswers & A>;
    prompts: {
        [x: string]: LegacyPromptConstructor | PromptFn<any, any>;
    };
    registerPrompt(name: string, prompt: LegacyPromptConstructor | PromptFn): /*elided*/ any;
    restoreDefaultPrompts(): void;
};
declare function registerPrompt(name: string, newPrompt: LegacyPromptConstructor): void;
declare function restoreDefaultPrompts(): void;
declare const inquirer: {
    prompt: {
        <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: (UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never> & {
            name: Extract<keyof PrefilledAnswers, string> | Extract<keyof A, string>;
        })[], answers?: PrefilledAnswers | undefined): PromptReturnType<PrefilledAnswers & A extends infer T_1 ? { [K in keyof T_1]: (PrefilledAnswers & A)[K]; } : never>;
        <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: { [name in keyof A]: UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never>; }, answers?: PrefilledAnswers | undefined): PromptReturnType<PrefilledAnswers & Answers<Extract<keyof A, string>> extends infer T_1 ? { [K_1 in keyof T_1]: (PrefilledAnswers & Answers<Extract<keyof A, string>>)[K_1]; } : never>;
        <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: Observable<UnnamedDistinctQuestion<PrefilledAnswers & A extends infer T ? { [K in keyof T]: (PrefilledAnswers & A)[K]; } : never> & {
            name: Extract<keyof PrefilledAnswers, string> | Extract<keyof A, string>;
        }>, answers?: PrefilledAnswers | undefined): PromptReturnType<PrefilledAnswers & A extends infer T_1 ? { [K in keyof T_1]: (PrefilledAnswers & A)[K]; } : never>;
        <const A extends Answers, PrefilledAnswers extends Answers = object>(questions: UnnamedDistinctQuestion<A & PrefilledAnswers> & {
            name: Extract<keyof A, string> | Extract<keyof PrefilledAnswers, string>;
        }, answers?: PrefilledAnswers | undefined): PromptReturnType<PrefilledAnswers & A>;
        prompts: {
            [x: string]: LegacyPromptConstructor | PromptFn<any, any>;
        };
        registerPrompt(name: string, prompt: LegacyPromptConstructor | PromptFn): /*elided*/ any;
        restoreDefaultPrompts(): void;
    };
    ui: {
        Prompt: typeof PromptsRunner;
    };
    createPromptModule: typeof createPromptModule;
    registerPrompt: typeof registerPrompt;
    restoreDefaultPrompts: typeof restoreDefaultPrompts;
    Separator: typeof Separator;
};
export default inquirer;
