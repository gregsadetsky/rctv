/// <reference lib="dom" />
/// <reference lib="dom.iterable" />

declare global {
  interface Window {
    RC: any;
  }
}

const SDK_LOADED_END = "sdkLoadedEnd";

// Fetches signed in users from the RC API using the given RC Personal Access
// Token
const getSignedInUsers = async () => {
  const res = await fetch(`${process.env.API_SERVER_URL}/api/hubVisits`, {
    credentials: "include",
  });
  const data = await res.json();
  return data;
};

// Calls the developer provided function when ready
const onLoad = (clientOnLoadCallback: () => void) => {
  // Tell parent rctv iframe that onLoad was called so it can stop its 30 second kill timer
  window.parent.postMessage(
    {
      type: SDK_LOADED_END,
    },
    "*"
  );

  // good to go, let's go
  clientOnLoadCallback();
};

var RC = {
  onLoad,
  getSignedInUsers,
};

// Global expor
window.RC = RC;
