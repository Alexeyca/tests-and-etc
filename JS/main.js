module.exports = function sortCategoriesForInsert(entryArray, id=null){
    var sorted=[];
    for(item of entryArray){
        if (item.parent_id===id){
            sorted=sorted.concat(item);
            sorted=sorted.concat(sortCategoriesForInsert(entryArray,item.id));
        }
    }
    return sorted
}