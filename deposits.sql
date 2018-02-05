SELECT      
    TXO.Value, B.ID, TX.ID, TX.TXID, TXO.[Index], TXO.ID
FROM
    TransactionOutput TXO INNER JOIN
    [Transaction] TX ON TXO.TransactionID = TX.ID INNER JOIN
    Block B ON TX.BlockID = B.ID 
WHERE
    TXO.ToAddress = '$_BTC_ADDR' AND
    B.BranchID = $_BRANCH