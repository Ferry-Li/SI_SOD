import cv2
import os

vertical = (576, 768)
horizontal = (768, 568)

vertical_list = ['0026', 'ILSVRC2012_test_00020467']
horizontal_list = ['172032', '6163', '2205', '4066', 'sun_aolxbgnccbjmzwpi', 'sun_aihhvbrwwjffquxu', 'ILSVRC2012_test_00002009', '156079', '0466', '1033', '2076',
'2177', '2196', '2318']
horizontal_list
def resize_img(img_name, is_horizontal=True):
    img = cv2.imread(img_name)
    if is_horizontal:
        resized = cv2.resize(img, horizontal)
    else:
        resized = cv2.resize(img, vertical)
    
    return resized
    
    
    
if __name__ == "__main__":
    for img_name in horizontal_list:
        img = img_name + '.png'
        origin_mask = img_name + '_Origin.png'
        our_mask = img_name + '_Ours.png'
        
        resized_img = resize_img(img)
        resized_origin_mask = resize_img(origin_mask)
        resized_our_mask = resize_img(our_mask)
        
        cv2.imwrite(os.path.join('new', img), resized_img)
        cv2.imwrite(os.path.join('new', origin_mask), resized_origin_mask)
        cv2.imwrite(os.path.join('new', our_mask), resized_our_mask)
    
    for img_name in vertical_list:
        img = img_name + '.png'
        origin_mask = img_name + '_Origin.png'
        our_mask = img_name + '_Ours.png'
        
        resized_img = resize_img(img, False)
        resized_origin_mask = resize_img(origin_mask, False)
        resized_our_mask = resize_img(our_mask, False)
        
        cv2.imwrite(os.path.join('new', img), resized_img)
        cv2.imwrite(os.path.join('new', origin_mask), resized_origin_mask)
        cv2.imwrite(os.path.join('new', our_mask), resized_our_mask)