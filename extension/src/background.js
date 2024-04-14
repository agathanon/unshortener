const shortenerDomains = [
    "t.co"
];

browser.contextMenus.create({
        id: "unshorten-link",
        title: "Unshorten link",
        contexts: ["link"],
    },
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
    fetch("http://localhost:8000/?url=" + linkUrl)
    .then(res => {
        if (!res.ok) {
            console.log("Couldn't unshorten URL: " + res.statusText);
        }
        return res.json();
    })
    .then(unshortenedUrl => {
        console.log("unshortened: " + unshortenedUrl)
        navigator.clipboard.writeText(unshortenedUrl)
        .catch(err => console.error("Couldn't copy to clipboard: ", err));
    })
    .catch(err => {console.error("Couldn't contact server:", err)});
}