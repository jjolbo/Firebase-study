import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as firebase from 'firebase';

  const config = {
    apiKey: "api key",
    authDomain: "*****.firebaseapp.com",
    databaseURL: "https://********.firebaseio.com",
    storageBucket: "*********.appspot.com"
  }; 
  
firebase.initializeApp(config);


ReactDOM.render(
<App />, 
document.getElementById('root')
);
