// const server = http.createServer((req, res) => {
//     let filePath = req.url === '/' ? 'index.html' : req.url.slice(1); // Assuming index.html is in the root directory

//     const extname = path.extname(filePath);
//     let contentType = 'text/html';

//     switch (extname) {
//         case '.js':
//             contentType = 'text/javascript';
//             break;
//         case '.css':
//             contentType = 'text/css';
//             break;
//     }

//     filePath = path.join(__dirname, filePath);

//     fs.readFile(filePath, (err, content) => {
//         if (err) {
//             if (err.code === 'ENOENT') {
//                 // File not found
//                 res.writeHead(404);
//                 res.end(`File ${filePath} not found`);
//             } else {
//                 // Server error
//                 res.writeHead(500);
//                 res.end(`Server error: ${err.code}`);
//             }
//         } else {
//             // Success
//             res.writeHead(200, { 'Content-Type': contentType });
//             res.end(content, 'utf-8');
//         }
//     });
// });

// server.js

const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000; // Use port 3000 by default

// Serve static files (index.html, styles.css, index.js, etc.)
app.use(express.static(path.join(__dirname)));

// Define a route to serve index.html
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
