// src: https://responsive-muse.com/export-youtube-playlist-video-urls-titles-js/
let goToBottom = setInterval(() => window.scrollBy(0, 400), 1000);

clearInterval(goToBottom);
let arrayVideos = [];
console.log('\n'.repeat(50));
const links = document.querySelectorAll('a');
for (const link of links) {
if (link.id === "video-title") {
    link.href = link.href.split('&list=')[0];
    arrayVideos.push(link.title + ';' + link.href);
    console.log(link.title + '\t' + link.href);
}
}


let data = arrayVideos.join('\n');
let blob = new Blob([data], {type: 'text/csv'});
let elem = window.document.createElement('a');
elem.href = window.URL.createObjectURL(blob);
elem.download = 'codex_playlist.csv';
document.body.appendChild(elem);
elem.click();
document.body.removeChild(elem);