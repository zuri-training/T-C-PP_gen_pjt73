class Form {
    constructor(form, fields) {
        this.form = form;
        this.fields = fields;
        this.validateonSubmit();
    }
    
    validateonSubmit() {
        let self = this; // setup calls to the "this" values of the class described in the constructor
        
        // add a submit event listener to the form
        this.form.addEventListener("submit", event => {
            // prevent default action
            event.preventDefault();
            let error = 0;
             // loop through the fields and check them against a function for validation
            self.fields.forEach(field => {
                const input = document.querySelector(`#${field}`);
                // if a field does not validate, auto-increment our error integer
                if (self.validateFields(input) === false) {
                    error++;
                }
            })
            // if everything validates, error will be 0 and can continue
            if (error === 0) {
                // do login api here or in this case, just submit the form and set a localStorage item
                this.form.submit();
            }
        })
    }

    validateFields(field) {
        // remove any whitespace and check to see if the field is blank, if so return false
        if(field.value.trim() === "") {
            // set the status based on the field, the field label, and if it is an error message
            this.setStatus(
                field,
                `${field.parentElement.previousElementSibling.innerText} cannot be blank`,
                "error"
            )
            return false;
        }
        
        else {
            // if the field is not blank, check to see if it is the password
            if (field.type === "password") {

                // store the password and confirm password values into variables so that they can be compared
                const password = document.querySelector("#password").value;
                const confirmPassword = document.querySelector("#confirm-password").value;

                // check if the password and confirm password inputs are the same
                if (password !== confirmPassword) {
                    this.setStatus(
                        field,
                        "passwords do not match",
                        "error"
                    )
                    return false;
                }

                // if it is a password, check to see if it meets our minimum character requirement
                if (field.value.length < 8) {

                    // set the status based on the field, the field label, and if it is an error message
                    this.setStatus(
                        field,
                        `${field.parentElement.previousElementSibling.innerText} must be at least 8 characters`,
                        "error"
                    )
                    return false;
                }
                else {
                    // set the status based on the field without text and return a success message
                    this.setStatus(field, null, "success");
                    return true;
                }
            }

            else {
                // set the status based on the field without text and return a success message
                this.setStatus(field, null, "success");
                return true;
            }
        }
    }
    
    setStatus(field, message, status) {

        // create variable to hold the error message span element
        const errorMessage = field.parentElement.nextElementSibling;

        // if success, remove messages and error classes
        if (status === "success") {
            if(errorMessage) {
                errorMessage.innerText = "";
            }
            field.classList.remove("input-error");
        }
        // if error, add messages and add error classes
        if (status === "error") {
            errorMessage.innerText = message;
            field.classList.add("input-error");
        }
    }
}

// create a variable for the login form
const form = document.querySelector("form");

// if the form exists, run the class
if (form) {
    // setup the form fields we want to validate
    const fields = ["e-mail", "password", "confirm-password"];
    // run the class
    const validator = new Form(form, fields);
}