import React, { Component, useState } from 'react'
import { observer } from 'mobx-react'
import { useStores } from 'hooks'


export const CreatePlaylist = observer(() => {
  const { playlistStore } = useStores()
  const convertPlaylist = async (playlistId) => {
    const tracks = await playlistStore.fetchTracksFromPlaylist(playlistId)
    console.log(tracks)
    playlistStore.getSamplesFromTrackList(tracks)
  }
  return (
    <div className="App">
      <div className="App-header">
        <ul>
          {playlistStore.tracks.map((e: any) => <li><small>{e.track.name}</small></li>)}
        </ul>
        <button onClick={() => convertPlaylist('6dhvndQ40s8iNmvWKKLLFQ') }>Fetch</button>
      </div>
    </div>
  );
})
