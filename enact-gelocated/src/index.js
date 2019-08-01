import React from 'react';
import {render} from 'react-dom';
import App from './App';
import * as firebase from 'firebase';


const config = {
    apiKey: "***********",
    authDomain: "*******.firebaseapp.com",
    databaseURL: "https://********.firebaseio.com",
    storageBucket: "*********.appspot.com"
  };

firebase.initializeApp(config);

const appElement = (<App />);

// In a browser environment, render instead of exporting
if (typeof window !== 'undefined') {
	render(appElement, document.getElementById('root'));
}

export default appElement;
