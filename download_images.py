from google_images_search import GoogleImagesSearch
import urllib.request

# Create a search object
gis = GoogleImagesSearch('your_dev_api_key', 'your_project_cx') #get the keys from GCP console
def download_img(keyword,img_count):
    # Set the search parameters
    search_params={"q":keyword,'num': img_count,
        'fileType': 'jpg',}
    gis.search(search_params)

    # Get the search results
    results = gis.results()

    # Iterate through the results and download each image
    i=0
    print(len(results))
    for result in results:
        try:
            url = result.url
            response = urllib.request.urlopen(url)
            file = open(str(i)+'.jpg', 'wb')
            file.write(response.read())
            i+=1
            file.close()
            print('Saved image')
        except Exception as e:
            print(e)

download_img('damaged cars',20)