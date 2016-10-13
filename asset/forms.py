import os
import random
import logging
from django import forms
from datetime import date
from models import Item, Positions, Custodian, Question, StkCat, TmpPlInvoice, TmpPlInvoicedet
from django.forms import ModelForm, ModelChoiceField

choices = tuple()
count = 0
for item in Item.objects.values('description'):
    count += 1
    choices += (str(count), item)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_path = os.path.join(BASE_DIR, 'media')
static_path = os.path.join(BASE_DIR, 'static')
logger = logging.getLogger(__name__)


class ItemComboForm(forms.ModelForm):
    new_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}))

    class Meta:
        model = Item
        exclude = ['post_date', 'inactive', 'staxp', 'o_rate', 'unit', 'specs', 'o_qty', 'stock_code', 'cat_id']
        widgets = {
            'description': forms.Select(choices=Item.objects.all().values_list('stock_code', 'description'), attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'})
        }
        labels = {
            'description': 'Assets'
        }


class PosComboForm(forms.ModelForm):
    class Meta:
        model = Positions
        exclude = ['pos_code']
        widgets = {
            'description': forms.Select(choices=Positions.objects.all().values_list('pos_code', 'description'), attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'})
        }
        labels = {
            'description': 'Locations'
        }


class CusComboForm(forms.ModelForm):
    class Meta:
        model = Custodian
        exclude = ['acct_id']
        widgets = {
            'description': forms.Select(choices=Custodian.objects.all().values_list('acct_id', 'description'), attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'})
        }
        labels = {
            'description': 'Custodians',
        }


class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.description


class TmpFormm(forms.ModelForm):
    pos_code = MyModelChoiceField(queryset=Positions.objects.all(), widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    cust = MyModelChoiceField(queryset=Custodian.objects.all(), to_field_name='acct_id',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    acct = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))

    voucher_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}))
    temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
    logger.info('Voucher ID already present %s', temp_vid)
    if not temp_vid:
        voucher_id = str(1).zfill(4)
    else:
        voucher_id = str(int(max(temp_vid)) + 2).zfill(4)

    class Meta:
        model = TmpPlInvoice
        exclude = ['net_amt', 'post_date', 'address', 'posted']

        temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
        logger.info('Voucher ID already present %s', temp_vid)
        if not temp_vid:
            voucher_id = str(1).zfill(4)
        else:
            voucher_id = str(int(max(temp_vid)) + 2).zfill(4)

        widgets = {
                    'voucher_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required':'False', 'name': 'voucher_id', 'readonly': 'readonly', 'value': voucher_id}),
                    'voucher_date': forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1','aria-describedby': 'inputSuccess2Status'}),
                    'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False'}),
                }
        labels = {
                    'pos_code': 'Locations',
                    'cust': 'Custodians',
                    'acct': 'Items'

                }


class MyyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.description


class TmpFormDetFormm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     voucher = kwargs.pop('voucher', None)
    #     super(TmpFormDetForm, self).__init__(*args, **kwargs)
    #     print 'lokk at this', voucher
        # TmpPlInvoicedet.objects.create(voucher=TmpPlInvoice.objects.get(voucher_id=voucher))
        # self.fields['voucher'].initial = voucher


    # stock_code = MyyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
    #                               widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    # serial = forms.BooleanField(
    #     widget=forms.CheckboxInput(attrs={'tabindex': '-1', 'class': 'flat', 'required': 'False'}))
    #


    class Meta:
        model = TmpPlInvoicedet
        exclude = ['emp_id', 'stock_code', 'particulars', 'rate', 'itemtot', 'voucher', 'lineitem']
        widgets = {
            'voucher': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'name': 'voucher',
                       'readonly': 'readonly'}),
            'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False',  'blank': 'True'}),
            'qty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'required': 'False',  'blank': 'True'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Rate', 'required': 'False',  'blank': 'True'}),
            'itemtot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Total', 'required': 'False',  'blank': 'True'}),
            'lineitem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Total', 'required': 'False',  'blank': 'True'}),
        }

        labels = {
            'qty': 'Quantity',
            'itemtot': 'Item Total'
        }



class TmpFor(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        voucher_id = kwargs.pop('voucher_id', None)
        super(TmpFor, self).__init__(*args, **kwargs)
        self.fields['voucher_id'].initial = voucher_id

    pos_code = MyModelChoiceField(queryset=Positions.objects.all(), widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    cust = MyModelChoiceField(queryset=Custodian.objects.all(), to_field_name='acct_id',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    acct = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))

    voucher_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}))

    class Meta:
        model = TmpPlInvoice
        exclude = ['net_amt', 'post_date', 'address', 'posted']
        widgets = {
                    'voucher_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required':'False', 'name': 'voucher_id', 'readonly': 'readonly'}),
                    'voucher_date': forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1','aria-describedby': 'inputSuccess2Status'}),
                    'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False'}),
                }
        labels = {
                    'pos_code': 'Locations',
                    'cust': 'Custodians',
                    'acct': 'Items'

                }

class NameForm(forms.Form):
    combo_final = ([('', 'Select One')])
    combo_final1 = ([('', 'Select One')])
    combo_final2 = ([('', 'Select One')])
    combo_final3 = ([('', 'Select One')])

    items = list(Item.objects.all().values_list('stock_code', 'description'))
    item_final = combo_final.extend(items)
    item_combo = forms.CharField(widget=forms.Select(choices=combo_final, attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'}))

    temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
    if not temp_vid:
        voucher_id = 0
        voucher_id += 1
    else:
        voucher_id = str(int(max(temp_vid)) + 2).zfill(4)

    new_parc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False'}))
    new_vid = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required':'False', 'name': 'voucher_id', 'readonly': 'readonly', 'value': voucher_id}))
    new_date = forms.DateField(widget=forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1','aria-describedby': 'inputSuccess2Status'}))


    pos = Positions.objects.all().values_list('pos_code', 'description')
    pos_final = combo_final1.extend(pos)
    pos_combo = forms.CharField(widget=forms.Select(choices=combo_final1, attrs={ 'class': 'select2_single form-control', 'id': 'new_loc', 'blank': 'True'}))



    cus = Custodian.objects.all().values_list('acct_id', 'description')
    cus_final = combo_final2.extend(cus)
    cus_combo = forms.CharField(widget=forms.Select(choices=combo_final2,
                                                    attrs={'class': 'select2_single form-control', 'id': 'new_cus',
                                                           'blank': 'True'}))


class AddRowsForm(forms.Form):
    combo_final4 = ([('', 'Select One')])
    items = list(Item.objects.all().values_list('stock_code', 'description'))
    item_final = combo_final4.extend(items)

    Serial = forms.BooleanField(widget=forms.CheckboxInput(attrs={'tabindex': '-1', 'class': 'flat', 'required':'False'}))
    # table_index = forms.CharField(widget=forms.HiddenInput(attrs={'required': 'False'}))
    Particulars = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Add Particulars', 'required':'False'}))
    Quantity = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'required':'False'}))
    Rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Rate', 'required':'False'}))
    Amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Amount', 'required':'False'}))
    StockCode = forms.IntegerField(widget=forms.Select(choices=combo_final4, attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'}))


class NameeeeForm(forms.Form):
    new_parc = forms.CharField(max_length=200, required=False)
    new_vid = forms.CharField(max_length=50, required=False)
    # new_date = forms.DateField(initial=datetime.date.today, required=False, error_messages={'required': 'Your Name is Required'})
    item_combo = forms.IntegerField(widget=forms.Select(choices=Item.objects.all().values_list('cat_id', 'description'),
                                                        attrs={'tabindex': '-1', 'class': 'select2_single form-control', 'id':'new_item'})) #check for the cross sign
    pos_combo = forms.IntegerField(widget=forms.Select(choices=Positions.objects.all().values_list('pos_code', 'description'),
                                                        attrs={'tabindex': '-1', 'class': 'select2_single form-control',
                                                               'id': 'new_item'}))  # check for the cross sign
    cust_combo = forms.IntegerField(widget=forms.Select(choices=Custodian.objects.all().values_list('acct_id', 'description'),
                                                        attrs={'tabindex': '-1', 'class': 'select2_single form-control',
                                                               'id': 'new_item'}))  # check for the cross sign

    table_checkbox = forms.BooleanField(widget=forms.CheckboxInput(attrs={'tabindex': '-1', 'class': 'flat', 'required':'False'}))
    table_parc = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False'}))
    table_qty = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Quantity', 'required':'False'}))
    table_rate = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Rate', 'required':'False'}))
    table_amount = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Amount', 'required':'False'}))
    table_scode = forms.IntegerField(widget=forms.Select(choices=Item.objects.all().values_list('cat_id', 'description'),
                                                        attrs={'tabindex': '-1', 'class': 'select2_single form-control', 'id':'new_item'}))


class NameeForm(forms.Form):
    new_parc = forms.CharField(max_length=200, required=False)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    file = forms.FileField(required=False)


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class LinkForm(forms.Form):
    """
    Form for individual user links
    """
    anchor = forms.CharField(
                    max_length=100,
                    widget=forms.TextInput(attrs={
                        'placeholder': 'Link Name / Anchor Text',
                    }),
                    required=False)
    url = forms.URLField(
                    widget=forms.URLInput(attrs={
                        'placeholder': 'URL',
                    }),
                    required=False)


class ProfileForm(forms.Form):
    """
    Form for user to update their own profile details
    (excluding links which are handled by a separate formset)
    """
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['first_name'] = forms.CharField(
                                        max_length=30,
                                        initial = self.user.first_name,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'First Name',
                                        }))
        self.fields['last_name'] = forms.CharField(
                                        max_length=30,
                                        initial = self.user.last_name,
                                        widget=forms.TextInput(attrs={
                                            'placeholder': 'Last Name',
                                        }))


from django.forms.formsets import BaseFormSet


class BaseLinkFormSet(BaseFormSet):
    def clean(self):
        """
        Adds validation to check that no two links have the same anchor or URL
        and that all links have both an anchor and URL.
        """
        if any(self.errors):
            return

        anchors = []
        urls = []
        duplicates = False

        for form in self.forms:
            if form.cleaned_data:
                anchor = form.cleaned_data['anchor']
                url = form.cleaned_data['url']

                # Check that no two links have the same anchor or URL
                if anchor and url:
                    if anchor in anchors:
                        duplicates = True
                    anchors.append(anchor)

                    if url in urls:
                        duplicates = True
                    urls.append(url)

                if duplicates:
                    raise forms.ValidationError(
                        'Links must have unique anchors and URLs.',
                        code='duplicate_links'
                    )

                # Check that all links have both an anchor and URL
                if url and not anchor:
                    raise forms.ValidationError(
                        'All links must have an anchor.',
                        code='missing_anchor'
                    )
                elif anchor and not url:
                    raise forms.ValidationError(
                        'All links must have a URL.',
                        code='missing_URL'
                    )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('answered',)


class PForm(forms.Form):
    combo_final = ([('', 'Select One')])
    combo_final1 = ([('', 'Select One')])
    combo_final2 = ([('', 'Select One')])
    combo_final3 = ([('', 'Select One')])

    items = list(Item.objects.all().values_list('stock_code', 'description'))
    item_final = combo_final.extend(items)

    pos = Positions.objects.all().values_list('pos_code', 'description')
    pos_final = combo_final1.extend(pos)

    cus = Custodian.objects.all().values_list('acct_id', 'description')
    cus_final = combo_final2.extend(cus)

    cat = StkCat.objects.all().values_list('cat_id', 'description')
    cat_final = combo_final3.extend(items)

    vid = forms.CharField(
        widget=forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control', 'placeholder': '', 'blank': 'True'}), required=False)

    from_date = forms.DateField(widget=forms.TextInput(attrs={ 'class': 'form-control has-feedback-left', 'id': 'single_cal1','aria-describedby': 'inputSuccess2Status', 'blank': 'True'}))

    to_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal2',
               'aria-describedby': 'inputSuccess2Status', 'blank': 'True'}))

    loc_combo = forms.IntegerField(widget=forms.Select(choices=combo_final1, attrs={ 'class': 'select2_single form-control', 'id': 'new_loc', 'blank': 'True'}))

    cus_combo = forms.IntegerField(widget=forms.Select(choices=combo_final2, attrs={'class': 'select2_single form-control', 'id': 'new_cus', 'blank': 'True'}))

    item_combo = forms.IntegerField(widget=forms.Select(choices=combo_final, attrs={'class': 'select2_single form-control', 'id': 'new_item', 'blank': 'True'}))

    cat_combo = forms.IntegerField(widget=forms.Select(choices=combo_final3, attrs={ 'class': 'select2_single form-control', 'id': 'new_cat', 'blank': 'True'}))



################################################################
                # Working copies
################################################################

class CopyTmpForm(forms.ModelForm):
    pos_code = MyModelChoiceField(queryset=Positions.objects.all(), widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    cust = MyyModelChoiceField(queryset=Custodian.objects.all(), to_field_name='acct_id',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))
    acct = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}))

    voucher_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}))

    class Meta:
        model = TmpPlInvoice
        exclude = ['net_amt', 'post_date', 'address', 'posted']

        temp_vid = TmpPlInvoice.objects.order_by().values_list("voucher_id", flat=True).distinct()
        logger.info('Voucher ID already present %s', temp_vid)
        if not temp_vid:
            voucher_id = str(1).zfill(4)
        else:
            voucher_id = str(int(max(temp_vid)) + 1).zfill(4)

        widgets = {
                    'voucher_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required':'False', 'name': 'voucher_id', 'readonly': 'readonly', 'value': voucher_id}),
                    'voucher_date': forms.TextInput(attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1','aria-describedby': 'inputSuccess2Status'}),
                    'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Particulars', 'required':'False'}),
                }
        labels = {
                    'pos_code': 'Locations',
                    'cust': 'Custodians',
                    'acct': 'Items'

                }













from django.forms import ModelForm
from models import Author


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']


# class CopyTmpForm(ModelForm):
#     def __init__(self, *args, **kwargs):
#         voucher_id = kwargs.pop('voucher_id', None)
#         super(CopyTmpForm, self).__init__(*args, **kwargs)
#         self.fields['voucher_id'].initial = voucher_id
#
#     pos_code = MyModelChoiceField(queryset=Positions.objects.all(),
#                                   widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}), required=False)
#     cust = MyModelChoiceField(queryset=Custodian.objects.all(), to_field_name='acct_id',
#                               widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}), required=False)
#     acct = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
#                               widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}), required=False)
#
#     voucher_date = forms.DateField(widget=forms.TextInput(
#     attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
#            'aria-describedby': 'inputSuccess2Status'}), required=False)
#
#     class Meta:
#         model = TmpPlInvoice
#         exclude = ['net_amt', 'post_date', 'address', 'posted']
#         widgets = {
#             'voucher_id': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'name': 'voucher_id',
#                        'readonly': 'readonly'}),
#             'voucher_date': forms.TextInput(
#                 attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
#                        'aria-describedby': 'inputSuccess2Status'}),
#             'particulars': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': '', 'required': 'False'}),
#         }
#         labels = {
#             'pos_code': 'Locations',
#             'cust': 'Custodians',
#             'acct': 'Items'
#
#         }


class CopyTmpFormDetForm(forms.ModelForm):
    stock_code = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True', 'null' : 'True', 'required': 'False'}), required=False)

    class Meta:
        model = TmpPlInvoicedet
        exclude = ['emp_id', 'particulars', 'voucher', 'lineitem', 'id', ]
        widgets = {
            'voucher': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'name': 'voucher','readonly': 'readonly'}),
            'particulars': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required':'False',  'blank': 'True', 'null' : 'True'}),
            'qty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False',  'blank': 'True', 'null' : 'True'}),
            'rate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False',  'blank': 'True', 'null' : 'True'}),
            'itemtot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False',  'blank': 'True', 'null' : 'True'}),
            'lineitem': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False',  'blank': 'True', 'null' : 'True'}),

        }

        labels = {
            'qty': 'Quantity',
            'itemtot': 'Amount',
            'rate': 'Rate'
        }


class CopyTmpFormTotal(forms.ModelForm):

    class Meta:
        model = TmpPlInvoice
        exclude = ['post_date', 'address', 'posted', 'voucher_date', 'particulars', 'pos_code', 'cust', 'acct', 'voucher_id']
        widgets = {
                'net_amt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False',  'blank': 'True', 'null': 'True', 'align': 'right'}),
        }
        labels = {
            'net_amt': 'Total Amount',
        }



######################################
        # Master Detail Form
######################################
class TmpForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     voucher_id = kwargs.pop('voucher_id', None)
    #     super(TmpForm, self).__init__(*args, **kwargs)
    #     self.fields['voucher_id'].initial = voucher_id

    pos_code = MyModelChoiceField(queryset=Positions.objects.all(),
                                  widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}),
                                  required=False)
    cust = MyModelChoiceField(queryset=Custodian.objects.all(), to_field_name='acct_id',
                              widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}),
                              required=False)
    acct = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                              widget=forms.Select(attrs={'class': 'select2_single form-control', 'blank': 'True'}),
                              required=False)

    voucher_id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'name': 'voucher_id',
               'readonly': 'readonly'}), required=False)

    voucher_date = forms.DateField(widget=forms.TextInput(
        attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
               'aria-describedby': 'inputSuccess2Status'}), required=False)

    class Meta:
        model = TmpPlInvoice
        exclude = ['net_amt', 'post_date', 'address', 'posted']
        widgets = {

            'voucher_date': forms.TextInput(
                attrs={'tabindex': '-1', 'class': 'form-control has-feedback-left', 'id': 'single_cal1',
                       'aria-describedby': 'inputSuccess2Status'}),
            'particulars': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False'}),
        }
        labels = {
            'pos_code': 'Locations',
            'cust': 'Custodians',
            'acct': 'Items'

        }


class TmpFormDetForm(forms.ModelForm):
    stock_code = MyModelChoiceField(queryset=Item.objects.all(), to_field_name='stock_code',
                                    widget=forms.Select(
                                        attrs={'class': 'select2_single form-control', 'blank': 'True', 'null': 'True',
                                               'required': 'False'}), required=False)

    class Meta:
        model = TmpPlInvoicedet
        exclude = ['emp_id', 'particulars', 'voucher', 'lineitem', 'id', ]
        widgets = {
            'voucher': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'name': 'voucher',
                       'readonly': 'readonly'}),
            'particulars': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True',
                       'null': 'True'}),
            'qty': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True',
                       'null': 'True'}),
            'rate': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True',
                       'null': 'True'}),
            'itemtot': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True',
                       'null': 'True'}),
            'lineitem': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True',
                       'null': 'True'}),

        }

        labels = {
            'qty': 'Quantity',
            'itemtot': 'Amount',
            'rate': 'Rate'
        }


class TmpFormTotal(forms.ModelForm):
    class Meta:
        model = TmpPlInvoice
        exclude = ['post_date', 'address', 'posted', 'voucher_date', 'particulars', 'pos_code', 'cust', 'acct',
                   'voucher_id']
        widgets = {
            'net_amt': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '', 'required': 'False', 'blank': 'True', 'null': 'True',
                       'align': 'right'}),
        }
        labels = {
            'net_amt': 'Total Amount',
        }




