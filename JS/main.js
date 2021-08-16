module.exports = function sortCategoriesForInsert(entryArray, id=null){
    var sorted=[];
    for(x of entryArray){
        if (x.parent_id===id){
            sorted=sorted.concat(x);
            sorted=sorted.concat(sortCategoriesForInsert(entryArray,x.id));
        }
    }
    return sorted
}