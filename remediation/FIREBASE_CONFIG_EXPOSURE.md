# Remediation for FIREBASE_CONFIG_EXPOSURE

## Remediation Steps for Firebase Config Exposure

Firebase Config Exposure is a critical security issue that can lead to unauthorized access to your Firebase project. The following steps can help mitigate this vulnerability:

### Step 1: Remove Firebase credentials from the codebase

Check your codebase and remove the Firebase configuration from it. 

```javascript
// DO NOT DO THIS
var config = {
    apiKey: "<API_KEY>",
    authDomain: "<PROJECT_ID>.firebaseapp.com",
    databaseURL: "https://<DATABASE_NAME>.firebaseio.com",
    storageBucket: "<BUCKET>.appspot.com",
};
firebase.initializeApp(config);
```
Firebase configuration should never be exposed in your client-side codebase.

### Step 2: Utilize Environment Variables

Store your Firebase configuration details as environment variables. Use these environment variables in your codebase to initialize Firebase.

```javascript
// Use environment variables to store Firebase configuration details
var config = {
    apiKey: process.env.FIREBASE_API_KEY,
    authDomain: `${process.env.FIREBASE_PROJECT_ID}.firebaseapp.com`,
    databaseURL: `https://${process.env.FIREBASE_DATABASE_NAME}.firebaseio.com`,
    storageBucket: `${process.env.FIREBASE_BUCKET}.appspot.com`,
};
firebase.initializeApp(config);
```
Remember to never commit your .env or any file containing environment variables to the code repository. It is common practice to add .env to your .gitignore file.

### Step 3: Restrict Access using Firebase Rules

In your Firebase console, set Firebase Database and Storage rules. Configure them in such a way that only authenticated and authorized users can perform suitable operations.

For Firestore rules, the configuration might look something like:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    // Matches any document in the 'users' collection
    match /users/{userId} {
        // Allows read/write operations by authenticated users who have the same user_id as the document
        allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```