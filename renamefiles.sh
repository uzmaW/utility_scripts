str=$1;
strRep=$2;

find . -type f -name "*${str}*" | while read FILE ;do 
    newfile="$(echo ${FILE} | sed -e s/${str}/${strRep}/)" ; 
    echo "${newfile}"; 
    mv "${FILE}" "${newfile}"; 
done; 
