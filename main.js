const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');

let mainWindow;
let isKiosk = false;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 800,
    minWidth: 900,
    minHeight: 600,
    frame: false,
    titleBarStyle: 'hidden',
    backgroundColor: '#1a1a1a',
    icon: path.join(__dirname, 'icon.ico'),
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('index.html');

  // Prevent opening DevTools in production
  mainWindow.webContents.on('before-input-event', (event, input) => {
    if (input.key === 'F12' || (input.control && input.shift && input.key === 'I')) {
      event.preventDefault();
    }
  });

  // Prevent navigation to external URLs
  mainWindow.webContents.on('will-navigate', (event) => {
    event.preventDefault();
  });

  // Prevent new windows from opening
  mainWindow.webContents.setWindowOpenHandler(() => {
    return { action: 'deny' };
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

// Toggle kiosk mode — hides taskbar, notifications, everything
ipcMain.on('toggle-kiosk', () => {
  if (!mainWindow) return;
  isKiosk = !isKiosk;
  mainWindow.setKiosk(isKiosk);
  mainWindow.setAlwaysOnTop(isKiosk, 'screen-saver');
  mainWindow.setFullScreen(isKiosk);

  if (isKiosk) {
    // Block Alt+Tab, Alt+F4 etc by staying on top
    mainWindow.setSkipTaskbar(true);
    mainWindow.setMenuBarVisibility(false);
    mainWindow.focus();
  } else {
    mainWindow.setSkipTaskbar(false);
  }

  // Notify renderer of state change
  mainWindow.webContents.send('kiosk-state', isKiosk);
});

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  app.quit();
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
