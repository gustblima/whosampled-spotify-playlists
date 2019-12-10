import { observable, action, computed } from 'mobx'
import Api from 'Api'

export class AuthStore {
  @observable
  authToken: string = null

  constructor(private api: Api) {}

  @computed
  get isAuthenticated () {
    return Boolean(this.authToken)
  }

  @action
  setAuthToken (authToken: string) {
    this.authToken = authToken
    this.api.spotify.setToken(authToken)
  }

}