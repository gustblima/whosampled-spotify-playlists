import axios from 'axios'

const toData = (response: any) => response.data
export default class Api {
  private static instance: Api
  spotify = new SpotifyApi()
  scrape = new ScrapeApi()
  private constructor () {}

  static getInstance() {
    if(!Api.instance) {
      Api.instance = new Api()
    }
    return Api.instance
  }

}

class SpotifyApi {

  private api = axios.create({
    baseURL: 'https://api.spotify.com/v1',
  })

  constructor() {
    this.setToken(sessionStorage.getItem('t'))
  }
  createPlaylist(name: string, description: string, isPublic: boolean): Promise<any> {
    const body = {
        name,
        description,
        public: isPublic
    }
    return this.api.post('/playlists', body).then(toData)
  }

  addTracksToPlaylist(playlistId: string, tracks: string[]): Promise<any> {
    const params = {
        uris: tracks.join(',')
    }
    return this.api.post(`/playlists/${playlistId}/tracks`, { params }).then(toData)
  }

  getPlaylistInformation(playlistId: string) {
    return this.api.get(`/playlists/${playlistId}`).then(toData)
  }

  getPlaylistTracks(playlistId: string, offset: number = 0,  limit: number = 50): Promise<any> {
    const params = {
        limit: limit,
        offset: offset
    }
    return this.api.get(`/playlists/${playlistId}/tracks`, { params }).then(toData)
  }

  search(trackName: string, artistName: string, type: string = 'track', limit: number = 1): Promise<any> {
    const params = {
        q: `${trackName} ${artistName}`,
        type: type,
        limit: limit
    }
    return this.api.get('/search', { params }).then(toData)
  }

  setToken(token: string) {
    this.api.defaults.headers.common['Authorization'] = `Bearer ${token}`
    sessionStorage.setItem('t', token)
  }

}

class ScrapeApi {

  private api = axios.create({
    baseURL: process.env.REACT_APP_API_GATEWAY_ADDRESS
  })

}
