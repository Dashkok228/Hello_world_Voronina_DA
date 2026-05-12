SELECT product_id, COUNT(*) AS supplier_count
FROM product_suppliers
WHERE product_id IS NOT NULL
GROUP BY product_id
ORDER BY product_id ASC;