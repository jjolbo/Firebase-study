import React from 'react';
import {render} from 'react-dom';
import App from './App';
import * as firebase from 'firebase';


const config = {
    apiKey: "AIzaSyDD3MkGTwwXMTI0BZMXbpdfWGK3rd9Ppus",
    authDomain: "airpolice-123de.firebaseapp.com",
    databaseURL: "https://airpolice-123de.firebaseio.com",
    storageBucket: "airpolice-123de.appspot.com"
  };

firebase.initializeApp(config);

const appElement = (<App />);

// In a browser environment, render instead of exporting
if (typeof window !== 'undefined') {
	render(appElement, document.getElementById('root'));
}

export default appElement;
