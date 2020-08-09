import mega

m = Mega.from_credentials("lkmihnl@hi2.in","CRE7!S7F!jG-iD2")
                    filename=m.download_from_url(url)
                    print("Downloading Complete Mega :", filename)
