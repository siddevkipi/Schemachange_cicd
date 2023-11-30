def directory = "dbscripts/"
def pattern = /^[vV]\d+\.\d+\.\d+__[a-zA-Z0-9_]+\.sql$/

new File(directory).eachFile { file ->
    if (file.isFile()) {
        def fileName = file.name
        println(fileName)

        if (fileName =~ pattern) {
            println("File '$fileName' matches the pattern. Proceeding with schemachange.")
            println("Running schemachange")

            def schemachangeCommand = """
                schemachange -f ${file} -a ${System.getenv('SF_ACCOUNT')} \
                -u ${System.getenv('SF_USERNAME')} -r ${System.getenv('SF_ROLE')} \
                -w ${System.getenv('SF_WAREHOUSE')} -d ${System.getenv('SF_DATABASE')} \
                -c ${System.getenv('SF_DATABASE')}.SCHEMACHANGE.CHANGE_HISTORY --create-change-history-table
            """
            ProcessBuilder.parseCommandLine(schemachangeCommand).start().waitFor()

        } else {
            println("File '$fileName' does not match the pattern. Skipping schemachange.")
        }
    }
}
