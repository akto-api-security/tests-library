# Remediation for SENSITIVE_DATA_EXPOSURE_GOOGLE_FIREBASE_DATABASE_URL

## Remediation Steps for Sensitive Data Exposure for Google Firebase Database URL

### Step 1: Remove Firebase Database URL from Public Code
If your Firebase Database URL has been exposed publicly e.g., in your code repository, remove it immediately. Replace it with a placeholder.

```javascript
var config = {
apiKey: "<API_KEY>",
authDomain: "<PROJECT_ID>.firebaseapp.com",
databaseURL: "https://<DATABASE_NAME>.firebaseio.com", //remove hard coded URL
storageBucket: "<BUCKET>.appspot.com",
};
firebase.initializeApp(config);
```

### Step 2: Use Environment Variables
Store your Firebase Database URL in environment variables, so it is not exposed in your code.

```javascript
var config = {
apiKey: process.env.API_KEY,
authDomain: "<PROJECT_ID>.firebaseapp.com",
databaseURL: process.env.DATABASE_URL,
storageBucket: "<BUCKET>.appspot.com",
};
firebase.initializeApp(config);
```
### Step 3: Rules Configuration
Ensure to set up Firebase Database rules correctly to prevent unauthorized access. By default, Firebase data is readable and writable by any user. Modify rules as needed.

```json
{
  "rules": {
    ".read": "auth != null",
    ".write": "auth != null"
  }
}
```
### Step 4: Token-based authentication
Use Firebase Authentication to generate a sign-in token after the user signs in your app. And use this token to authenticate all requests to Firebase Database.

```javascript
firebase.auth().signInWithEmailAndPassword(email, password)
.then((userCredential) => {
let user = userCredential.user;
})
.catch((error) => {
console.log(error); 
});
```

### Step 5: Regular Audit and Updates
Regularly review your Firebase security rules and user permissions to prevent sensitive data exposure. Always keep your Firebase SDKs updated to the latest version. 

```bash
npm update firebase --save
```

Note: Replace <API_KEY>, <PROJECT_ID>, <DATABASE_NAME>, and "<BUCKET>" with your project's actual API key, Project ID, Database name, and bucket respectively.
Always remember to keep these values secret and do not expose them publicly. 

Remember, once your sensitive data is exposed on the internet it's nearly impossible to revoke access, always follow best practices to keep your data secure. Always make sure your security rules in Firebase are as tight and precise as possible.