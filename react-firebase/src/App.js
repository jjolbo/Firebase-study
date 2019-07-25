import React, { Component } from 'react';
import * as firebase from 'firebase';

class App extends Component {
  constructor() {
    super();
    this.state = {
      area1: 'none',
      area2: 'none',
      pm10Value: 'none',
      pm25Value: 'none',
      coValue: 'none'
    };
  }

  componentDidMount() {
    const rootRef = firebase.database().ref().child('서울');
    const areaRef = rootRef.child('강남구');
    const miseRef = areaRef.child('pm25Value');
    const ultraRef = areaRef.child('pm10Value');
    const coRef = areaRef.child('coValue');

    rootRef.on('value', snap => {
      this.setState({
        area1 : snap.key
      });
    });

    areaRef.on('value', snap => {
      this.setState({
        area2 : snap.key
      });
      console.log(this.state.area2);
    });

    miseRef.on('value', snap => {
      this.setState({
        pm25Value: snap.val()
      });
    });

    ultraRef.on('value', snap => {
      this.setState({
        pm10Value: snap.val()
      });
    });

    coRef.on('value', snap => {
      this.setState({
        coValue: snap.val()
      });
    });
  }

  render() {
    return (
      <div className="App">
        <h1>현재 지역 : {this.state.area1} {this.state.area2}</h1>
        <h2>pm25 농도(미세먼지) : {this.state.pm25Value}</h2>
        <h2>pm10 농도(초미세먼지): {this.state.pm10Value}</h2>
        <h2>일산화탄소 농도: {this.state.coValue} </h2>
      </div>
    )
  }
}

export default App;
