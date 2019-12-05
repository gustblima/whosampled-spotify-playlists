import React from 'react'
import { Router as ReactRouter, Route, Switch } from 'react-router-dom'
import { createBrowserHistory } from "history";
import { Main, CreatePlaylist } from './views'

const Router: React.SFC<any> = () => ( 
  <ReactRouter history={createBrowserHistory()}>
    <Switch>
      <Route exact path='/' component={Main} />
      <Route exact path='/playlist' component={CreatePlaylist} />
    </Switch>
  </ReactRouter> 
)

export default Router