music = require('musicmatch')({usertoken:"",format:"",appid:"437f020971788f570fb9683878c740e8"});

music.chartTracks({page:1,page_size:3,country:"tr",f_has_lyrics:1})
.then(function(data){
        console.log(data);
}).catch(function(err){
        console.log(err);
})