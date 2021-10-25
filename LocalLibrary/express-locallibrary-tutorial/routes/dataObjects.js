var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.send('Respond with a list of objects !');
});

module.exports = router;
