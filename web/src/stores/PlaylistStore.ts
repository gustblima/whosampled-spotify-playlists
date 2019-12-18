import { observable, action, runInAction } from 'mobx'
import Api from 'Api'
import { toJS } from 'mobx'

export class PlaylistStore {
  @observable tracks: any[] = []

  @observable sampledTracks: any[] = []

  @observable playlist: any

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

  @action
  getSamplesFromTrackList = async (tracks = [], size = 5) => {
    const formattedTracks = tracks.map(t => `${t.track.name} ${t.track.artists.map(a => a.name).join(' ')}`)

    let offset = 0
    let samples = []
    for(let i = 0; i * size < tracks.length; i++) {
      try {
        const data =  await this.api.scrape.getSamplesTracks(formattedTracks.splice(i * size, (i * size) + size))
        samples = samples.concat(data)
      } catch(e) {
        console.log(e)
      }
    }
    runInAction(() => {
      this.sampledTracks = samples
    })
    return this.sampledTracks
  }

}