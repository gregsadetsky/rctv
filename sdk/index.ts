/// <reference lib="dom" />
/// <reference lib="dom.iterable" />

const SDK_LOADED_START = "sdkLoadedStart";
const SDK_LOADED_END = "sdkLoadedEnd";

type API = {
  getSignedInUsers: () => void;
};

// Fetches signed in users from the RC API using the given RC Personal Access
// Token
const getSignedInUsers = async () => {
  const res = await fetch("http://localhost:8000/api/getHubVisits", {
    credentials: "include",
  });
  const data = await res.json();
  return data;
};

// Calls the developer provided function when ready
const onLoad = (theirs: (api: API) => void) => {
  // Tell parent (rctv) that onLoad was called so it can stop its 30 second timer
  window.parent.postMessage(
    {
      type: SDK_LOADED_END,
    },
    "*"
  );

  const API: API = {
    getSignedInUsers,
  };

  // Call the developer's function
  theirs(API);
};

document.addEventListener("DOMContentLoaded", () => {});

var RC = {
  onLoad,
};

// Global expor
window.RC = RC;
