// https://www.npmjs.com/package/react-geolocated
import React from 'react';
import {geolocated} from 'react-geolocated';
import * as firebase from  'firebase';

class Demo extends React.Component {
    render() {
		this.props.coords ? 
		(firebase.database().ref('/area/').set({'latitude': this.props.coords.latitude, 'longitude': this.props.coords.longitude}), 
		console.log(this.props.coords.latitude, this.props.coords.longitude))
		: console.log('Getting the location data')

		return(
			<div>
				hello!
			</div>
		);
    }
}

export default geolocated({
    positionOptions: {
        enableHighAccuracy: false,
    },
    userDecisionTimeout: 5000,
})(Demo);
