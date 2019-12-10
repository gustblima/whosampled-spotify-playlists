import React, { Component, useEffect } from 'react'
import { RouteComponentProps } from 'react-router'
import queryString from 'query-string'
import { useStores } from 'hooks'
import Api from 'Api'

export const AuthCallback = ({ history, location }) => {

  useEffect(() => {
    const { access_token } = queryString.parse(location.hash)
    if(!access_token) {
      history.push('/')
    } else {
      Api.getInstance().spotify.setToken(access_token as string)
      history.push('/create-playlist')
    }
  })

  return (
    <div className="App">
      <div className="App-header">
        <h2>Welcome to Create playlist</h2>
      </div>
    </div>
  );
}
