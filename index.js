const mongoose = require('mongoose');
const express = require('express');
const Crawling = require('./crawling');
const app = express();
const port = 3000;

let MONGO_URI = 'mongodb://localhost:27017/crawling_list';

mongoose.connect(MONGO_URI, { useMongoClient: true })
  .then(() => console.log('Successfully connected to mongodb'))
  .catch(e => console.error(e));

app.set('view engine', 'ejs');
app.engine('html', require('ejs').renderFile);

app.get('/', async (req, res) => {
  let crawlingList;

  await Crawling.find((err, data) => {
    if(err) return res.status(500).send({error : 'database failure'});
    crawlingList = data;
  });

  res.render('index', {crawlingList});
});

app.listen(port, () => {
  console.log(`Server On! port : ${port}`);
});