import React from 'react'
import { AuthStore, PlaylistStore } from 'stores'
import Api from 'Api'

const api = Api.getInstance()
export const storesContext = React.createContext({
  authStore: new AuthStore(api),
  playlistStore: new PlaylistStore(api)
})