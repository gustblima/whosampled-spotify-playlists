import React, { Component, useState } from 'react'
import { observer } from 'mobx-react'
import { useStores } from 'hooks'


export const CreatePlaylist = observer(() => {
  const { playlistStore } = useStores()
  return (
    <div className="App">
      <div className="App-header">
        <ul>
          <li>{playlistStore.tracks.map((e: any) => e.track.name)}</li>
        </ul>
        <button onClick={() => playlistStore.fetchTracksFromPlaylist('2OolXkqQ6n95xEYlGaAUfH')}>Fetch</button>
      </div>
    </div>
  );
})
