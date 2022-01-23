import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, PatternFill
from .models import Category,Crack,CrackObj

def facility(wb,pk):
  category = Category.objects.get(pk=pk)
  
  grayFill = PatternFill(start_color='CCCCCC',
                        end_color='CCCCCC', fill_type='solid')
  sheet = wb.worksheets[0]
  sheet.title = '시설물 현황'

  sheet = wb['시설물 현황']
  sheet['B2'] = "□ 시설물 현황"
  sheet['B3'] = "가. 일반현황"
  sheet['B12'] = "나. 전경사진"

  file_path = category.frontView.url
  path = file_path[1:]
  img = Image(path)
  sheet.add_image(img, "B13")

  sheet['B4'] = '시설물명'
  sheet['B5'] = '시설물위치'
  sheet['B6'] = '용도'
  sheet['B7'] = '구조형식'

  sheet['B4'].fill = grayFill
  sheet['B5'].fill = grayFill
  sheet['B6'].fill = grayFill
  sheet['B7'].fill = grayFill

  
  sheet.merge_cells('C4:D4')
  sheet.merge_cells('C5:D5')
  sheet.merge_cells('C6:D6')
  sheet.merge_cells('C7:D7')
  sheet['C4'] = category.facilityName
  sheet['C5'] = category.facilityNo
  sheet['C6'] = category.usage
  sheet['C7'] = category.structuralForm

  sheet['E4'] = "시설물번호"
  sheet['E5'] = "준공일자"
  sheet['E6'] = "시설물규모"
  sheet['E7'] = "부대시설"

  sheet['E4'].fill = grayFill
  sheet['E5'].fill = grayFill
  sheet['E6'].fill = grayFill
  sheet['E7'].fill = grayFill

  sheet.merge_cells('F4:G4')
  sheet.merge_cells('F5:G5')
  sheet.merge_cells('F6:G6')
  sheet.merge_cells('F7:G7')

  sheet['F4'] = category.facilityNo
  sheet['F5'] = category.completionDate
  sheet['F6'] = category.facilityStructure
  sheet['F7'] = category.amenities

  sheet['B8'] = '종별'
  sheet['D8'] = '전차안전등급'
  sheet['F8'] = '점검결과안전등급'

  sheet['B8'].fill = grayFill
  sheet['D8'].fill = grayFill
  sheet['F8'].fill = grayFill

  sheet['C8'] = category.floors
  sheet['E8'] = category.grade
  sheet['G8'] = category.testResults

  sheet.merge_cells('B9:G9')
  sheet.merge_cells('B10:G10')

  sheet['B9'] = '규모 및 제원 추가사항'
  sheet['B9'].fill = grayFill

  sheet['B10'] = category.plus

  sheet['B12'] = '나. 전경사진'
  path = category.frontView.url
  path = path[1:]
  img = Image(path)
  sheet.add_image(img,"B13")
  sheet.sheet_view.view = "pageBreakPreview"
  for row in sheet.rows:
      for cell in row:
          cell.alignment = Alignment(horizontal="center", vertical="center")
  return wb


def looks(wb,pk):
  unitCm = 10
  unitInch = round((unitCm/2.54)*70)
  
  cell = 2
  sheet = wb.create_sheet("외관조사사진", 1)
  sheet = wb['외관조사사진']
  crack = Crack.objects.get(pk=pk)
  crackObjs = CrackObj.objects.filter(parent=crack)
  for crackObj in crackObjs:
    path = (crackObj.image.url[1:])
    flatPath = (crackObj.flatting_image.url[1:])
    image = openpyxl.drawing.image.Image(path)
    flatImage = openpyxl.drawing.image.Image(flatPath)
    image.width = unitInch
    image.height = unitInch
    flatImage.height = unitInch
    flatImage.height = unitInch

    sheet.add_image(image,'B' + str(cell))
    sheet.add_image(flatImage, 'G'+ str(cell+1))
    cell += 5
  sheet.sheet_view.view = "pageBreakPreview"
  return wb