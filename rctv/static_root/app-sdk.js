// index.ts
var SDK_LOADED_END = "sdkLoadedEnd";
var getSignedInUsers = async () => {
  const res = await fetch("http://localhost:8000/api/getHubVisits", {
    credentials: "include"
  });
  const data = await res.json();
  return data;
};
var onLoad = (theirs) => {
  window.parent.postMessage({
    type: SDK_LOADED_END
  }, "*");
  const API = {
    getSignedInUsers
  };
  theirs(API);
};
document.addEventListener("DOMContentLoaded", () => {
});
var RC = {
  onLoad
};
window.RC = RC;
