import React, { Component } from 'react'

export class Homepage extends Component<any> {

  spotifyAuthenticationUrl = () => {
    return 'https://accounts.spotify.com/authorize' +
      `?response_type=token&client_id=${process.env.REACT_APP_SPOTIFY_CLIENT_ID}` +
      `&redirect_uri=${encodeURIComponent('http://' + window.location.host + '/callback')}`
  }

  render () {
    return (
      <div>
        <div>
          <a href={this.spotifyAuthenticationUrl()}>Login</a>
        </div>
      </div>
    );
  }
}
