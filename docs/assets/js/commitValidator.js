function commitValidator(commitText) {
    let haveType = false
    let haveBody = false

    const types = ["feat", "fix", "build", "chore", "ci", "docs", "style", "refactor", "perf", "test"]
    const typeRegex = new RegExp(`^\\b(${types.join("|")})\\b:`, "gi")
    console.log(typeRegex)

    if (typeRegex.test(commitText)) {
        console.log("Type found")
        haveType = true
    } else {
        console.log("Invalid commit: Missing type or invalid format");
    }

    const bodyRegex = new RegExp(`:[\w\s]+`)
    if (bodyRegex.test(commitText)){
        console.log("Body found")
    } else {
        console.log("Invalid commit: Missing body")
        haveBody = false
    }

    return (haveType && haveBody) ? true : false ;
}