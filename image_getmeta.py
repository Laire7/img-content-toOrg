from PIL import Image
from PIL.ExifTags import TAGS

# 이미지 파일 경로
image_path = 'C:/Users/park0/Downloads/IMG_5008.JPG'
output_path = 'image_metadata.txt'

def get_image_metadata(image_path):
    # 이미지 파일 열기
    image = Image.open(image_path)
    metadata = {}
    
    # EXIF 데이터 추출
    exif_data = image._getexif()
    if exif_data:
        for tag_id, value in exif_data.items():
            # 태그 ID를 사람이 읽을 수 있는 이름으로 변환
            tag_name = TAGS.get(tag_id, tag_id)
            metadata[tag_name] = value
    
    return metadata

# 메타데이터 추출 및 파일에 저장
metadata = get_image_metadata(image_path)
with open(output_path, 'w') as file:
    for key, value in metadata.items():
        file.write(f"{key}: {value}\n")

print(f"메타데이터가 '{output_path}'에 저장되었습니다.")
