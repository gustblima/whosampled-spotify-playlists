import React from 'react'
import { Router as ReactRouter, Route, Switch } from 'react-router-dom'
import { createBrowserHistory } from "history";
import { Homepage, CreatePlaylist, AuthCallback } from './views'

const Router: React.SFC<any> = () => ( 
  <ReactRouter history={createBrowserHistory()}>
    <Switch>
      <Route exact path='/' component={Homepage} />
      <Route exact path='/callback' component={AuthCallback} />
      <Route exact path='/create-playlist' component={CreatePlaylist} />
    </Switch>
  </ReactRouter> 
)

export default Router