// index.ts
var SDK_IS_AUTHENTICATED = false;
var SDK_LOADED_END = "sdkLoadedEnd";
var isSDKAuthenticated = async () => {
  if (SDK_IS_AUTHENTICATED) {
    return true;
  }
  const res = await fetch("https://rctv-dev.recurse.com/api/userIsAuthed", {
    credentials: "include"
  });
  const { user_is_authed } = await res.json();
  if (!user_is_authed) {
    const redirect_uri = encodeURIComponent(window.location.href);
    setTimeout(() => {
      window.location.href = `https://rctv-dev.recurse.com/developers?redirect_uri=${redirect_uri}`;
    }, 50);
    return false;
  } else {
    SDK_IS_AUTHENTICATED = true;
    return true;
  }
};
var apiFetcherFunctionMaker = (endpoint) => async (args) => {
  if (!await isSDKAuthenticated()) {
    return;
  }
  const res = await fetch(`https://rctv-dev.recurse.com/api/${endpoint}${args ? `?${new URLSearchParams(args)}` : ""}`, {
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
  getHubVisitsForToday: apiFetcherFunctionMaker("hubVisitsForToday"),
  getEvents: apiFetcherFunctionMaker("events")
};
