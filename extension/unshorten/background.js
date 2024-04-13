const shortenerDomains = [
    "t.co"
];

browser.contextMenus.create({
        id: "unshorten-link",
        title: "Unshorten link",
        contexts: ["link"],
    },
    // See https://extensionworkshop.com/documentation/develop/manifest-v3-migration-guide/#event-pages-and-backward-compatibility
    // for information on the purpose of this error capture.
    () => void browser.runtime.lastError,
);

browser.contextMenus.onClicked.addListener((info, tab) => {
    if (info.menuItemId === "unshorten-link") {
        const linkUrl = info.linkUrl;
        const linkDomain = getDomainFromUrl(linkUrl);
        const canShorten = shortenerDomains.includes(linkDomain);

        if (canShorten) {
            unshortenUrl(linkUrl);
        }
    }
});

function getDomainFromUrl(linkUrl) {
    const url = new URL(linkUrl);
    return url.hostname;
}

function unshortenUrl(linkUrl) {
    console.log(linkUrl);

    fetch("http://localhost:8000/?url=" + linkUrl)
    .then(res => {
        if (res.ok) {
            console.log(res);
        }
    });
}