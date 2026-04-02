const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('lockdown', {
  toggleKiosk: () => ipcRenderer.send('toggle-kiosk'),
  isElectron: true
});
