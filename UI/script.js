
var songs = []
function addSong(song_name) {
    const list = {
        "Virgos Groove": 0,
        "Poker Face": 1,
        "Jump": 2,
        "DaFunk": 3,
        "California Love": 4
    }

    alert(song_name + " added to queue");
    songs.push(song_name)
    //document.getElementById(list[song_name]).style.display = "none";


}

function downloadFile() {
    const a = document.createElement('a')
    var txt = ""
    for (var i = 0; i < songs.length; i++) {
        txt += songs[i]
        txt += '\n'
    }
    const blob = new Blob([txt], { type: 'text/csv' })
    const url = URL.createObjectURL(blob)
    a.setAttribute('href', url)
    a.setAttribute('download', "Playlist.txt")
    a.click() // Start downloading
    songs = []
}