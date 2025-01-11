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