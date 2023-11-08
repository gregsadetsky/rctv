// index.ts
var SDK_IS_AUTHENTICATED = false;
var SDK_LOADED_END = "sdkLoadedEnd";
var isSDKAuthenticated = async () => {
  if (SDK_IS_AUTHENTICATED) {
    return true;
  }
  const res = await fetch("http://localhost:8000/api/userIsAuthed", {
    credentials: "include"
  });
  const { user_is_authed } = await res.json();
  if (!user_is_authed) {
    alert("... start auth...");
  } else {
    SDK_IS_AUTHENTICATED = true;
    return true;
  }
};
var getHubVisitsForToday = async () => {
  if (!await isSDKAuthenticated()) {
    return;
  }
  const res = await fetch("http://localhost:8000/api/hubVisitsForToday", {
    credentials: "include"
  });
  const data = await res.json();
  return data;
};
var onLoad = (clientOnLoadCallback) => {
  window.parent.postMessage({
    type: SDK_LOADED_END
  }, "*");
  clientOnLoadCallback();
};
window.RC = {
  onLoad,
  getHubVisitsForToday
};
