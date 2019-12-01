
    
    
    let downloadedFromScript = false;
    let urlF;
    chrome.downloads.onDeterminingFilename.addListener(function(downloadItem, suggest) {
        let r = Math.floor(Math.random() * 1000).toString()
       
        if(downloadedFromScript){
        // name = r + downloadItem.id.toString() + downloadItem.filename;
        // suggest({filename: "bias/"+name, conflictAction: "overwrite" });
        // urlF = downloadItem.filename;
        // alert(urlF);
        // downloadedFromScript = false;

        

    }
      });


      chrome.runtime.onMessage.addListener( function(request,sender,sendResponse)
{
    if( request.greeting  === "Download")
    {
        
        downloadedFromScript = true;
          
    }
      })