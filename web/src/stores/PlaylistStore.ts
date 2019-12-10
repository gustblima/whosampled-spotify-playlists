import { observable, action, runInAction } from 'mobx'
import Api from 'Api'

export class PlaylistStore {
  @observable
  tracks: any[] = []

  @observable
  sampledTracks: any[] = []

  @observable
  playlist: any

  constructor(private api: Api) {}

  @action 
  fetchPlaylistInformation = async (playlistId: string) => {
    const playlist = await this.api.spotify.getPlaylistInformation(playlistId)
    runInAction(() => this.playlist = playlist)
  }

  @action
  fetchTracksFromPlaylist = async (playlistId: string) => {
    let hasNext = true
    let offset = 0
    let tracks = []
    while (hasNext) {
      const data = await this.api.spotify.getPlaylistTracks(playlistId, offset)
      tracks = tracks.concat(data.items)
      hasNext = Boolean(data.next)
      offset += data.items.length
    }
    runInAction(() => {
      this.tracks = tracks
    })
    return this.tracks
  }

}