from playwright.async_api import async_playwright
import os
import asyncio

async def test_upload():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        await page.goto("https://www.reduceimages.com/")
        
        image_folder_path = './image'
        
        file_names = os.listdir(image_folder_path)
        
        image_files = [file for file in file_names if file.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'))]
        
        if not os.path.exists('./resized'):
            os.makedirs('./resized')
        
        print("Image files to be processed:", image_files)
        
        for image in image_files:
            print("Processing:", image)
            async with page.expect_file_chooser() as fc_info:
                await page.click('xpath=//*[@id="dropzone-container-offline"]/div[2]/button')
            
            file_chooser = await fc_info.value
            await file_chooser.set_files(os.path.join(image_folder_path, image))
            
            await page.fill('xpath=//*[@id="width_field"]', "500")
            await page.fill('xpath=//*[@id="height_field"]', "500")
            await page.click('xpath=//*[@id="offline-submit-button"]')
            
            async with page.expect_download() as download_info:
                await page.click('xpath=//*[@id="download-button-container-cta"]')
            
            download = await download_info.value
            await download.save_as(os.path.join("./resized", download.suggested_filename))
        
        await page.wait_for_timeout(5000)
        
        await browser.close()

# Run the test_upload function
asyncio.run(test_upload())
