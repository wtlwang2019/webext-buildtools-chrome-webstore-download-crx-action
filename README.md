![Node.js CI](https://github.com/cardinalby/webext-buildtools-chrome-webstore-download-crx-action/workflows/build-test/badge.svg)

# Download crx of your WebExtension from Chrome Web Store

This action is experimental and uses undocumented Chrome Web Store endpoint.
Based on [typed-chrome-webstore-api](https://www.npmjs.com/package/typed-chrome-webstore-api) package.

It downloads crx of already published extension. To publish an extension in a workflow look at 
[upload](https://github.com/cardinalby/webext-buildtools-chrome-webstore-upload-action) and
[publish](https://github.com/cardinalby/webext-buildtools-chrome-webstore-publish-action) actions.

## Inputs

* `extensionId` **Required**<br>
Your extension id in Chrome Web Store
    
* `crxFilePath`**Required**<br>
Specify a relative file path to save crx file

* `prodVersion` Default: `83.0.4103.116`
Target version of Chrome, which must be 31.0.1609.0 at the very least

* `acceptFormat` Default: `crx2|crx3`
Accept crx file formats delimited by | sign. Allowed formats: `crx2`, `crx3`

* **Optionally** you can specify the following 3 inputs to point to exact platform 
you want to download crx for:
    * `downloadCrxPlatformOs` (`mac`, `win`, `android`, `cros`, `openbsd`, `Linux`)
    * `downloadCrxPlatformArch` (`arm`, `x86-64`, `x86-32`)
    * `downloadCrxPlatformNaclArch` (`arm`, `x86-64`, `x86-32`) 

## Outputs
 
* `crxFilePath` the absolute path to the downloaded crx file (if was)

## Usage example

```yaml
uses: cardinalby/webext-buildtools-chrome-webstore-download-crx-action@v1
with:
  extensionId: 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
  crxFilePath: 'build/extension.published.crx'
```

---
If you are interested in the building the entire deployment workflow for WebExtension, 
you can read this [article](https://cardinalby.github.io/blog/post/github-actions/webext/1-introduction/).