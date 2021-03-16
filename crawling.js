const mongoose = require('mongoose');

const crawlingSchema = new mongoose.Schema({
    tag_property: { type: String, required: true },
    content: { type : String }
},
{
    timestamps: true
});

module.exports = mongoose.model('crawling', crawlingSchema)