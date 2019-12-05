import React, { Component } from 'react'

export class Main extends Component {
  spotifyAuthenticationUrl = () => {
    return 'https://accounts.spotify.com/authorize' +
      `?response_type=code&client_id=${process.env.REACT_APP_SPOTIFY_CLIENT_ID}` +
      `&redirect_uri=${encodeURIComponent('http://localhost:3000')}`
  }


  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Welcome to Main</h2>
          <a href={this.spotifyAuthenticationUrl()}>BALBLABA</a>
        </div>
      </div>
    );
  }
}
